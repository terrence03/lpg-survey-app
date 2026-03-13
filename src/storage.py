# %%
import csv
import os
from datetime import datetime, timedelta, timezone
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

OUTPUT_DIR = "output"
CHECKIN_CSV = os.path.join(OUTPUT_DIR, "checkin.csv")
SURVEY_CSV = os.path.join(OUTPUT_DIR, "survey.csv")

CHECKIN_HEADERS = ["timestamp", "sid"]
SURVEY_HEADERS = [
    "timestamp", "sid", "q1", "q2", "q3", "gender", "age",
    "lpg_usage", "contract", "contract_no", "contract_no_other",
    "contract_aware", "contract_aware_no", "contract_aware_no_other",
    "contract_willing", "contract_willing_no", "contract_willing_no_other",
    "policy_info", "policy_info_network", "policy_info_network_other",
    "policy_info_advertising", "policy_info_advertising_other", "policy_info_other",
]


def _write_to_csv(filepath: str, headers: list, rows: list):
    """Append rows to a local CSV file, writing headers if the file is new."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    write_header = not os.path.exists(filepath)
    with open(filepath, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(headers)
        writer.writerows(rows)

# 設定 API 權限範圍
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
]

def get_timestamp() -> str:
    # Get the current time in UTC+8
    utc_now = datetime.now(timezone.utc)
    taipei_now = utc_now.astimezone(timezone(timedelta(hours=8)))
    return taipei_now.strftime("%Y-%m-%d %H:%M:%S")


def get_service_account_credentials() -> service_account.Credentials:
    """從設定檔案獲取服務帳戶認證資訊並建立憑證"""
    # 從TOML配置構建服務帳戶資訊
    service_account_info = st.secrets["gcp_service_account"]

    # 建立憑證物件
    credentials = service_account.Credentials.from_service_account_info(
        service_account_info, scopes=SCOPES
    )

    return credentials


def append_checkin_record(values):
    """
    Creates the batch_update the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = get_service_account_credentials()
    # pylint: disable=maybe-no-member
    try:
        service = build("sheets", "v4", credentials=creds)
        body = {"values": values}
        result = (
            service.spreadsheets()
            .values()
            .append(
                spreadsheetId=st.secrets["spreadsheet"]["check_in"],
                range="A1:B1",
                valueInputOption="USER_ENTERED",
                body=body,
            )
            .execute()
        )
        print(f"{(result.get('updates').get('updatedCells'))} cells appended.")
        return result

    except HttpError as error:
        print(f"An error occurred: {error}")
        print("Falling back to local CSV storage for checkin record.")
        _write_to_csv(CHECKIN_CSV, CHECKIN_HEADERS, values)
        return error


def append_survey_response(values):
    """
    Creates the batch_update the user has access to.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = get_service_account_credentials()
    # pylint: disable=maybe-no-member
    try:
        service = build("sheets", "v4", credentials=creds)
        body = {"values": values}
        result = (
            service.spreadsheets()
            .values()
            .append(
                spreadsheetId=st.secrets["spreadsheet"]["response"],
                range="A1:R1",
                valueInputOption="USER_ENTERED",
                body=body,
            )
            .execute()
        )
        print(f"{(result.get('updates').get('updatedCells'))} cells appended.")
        return result

    except HttpError as error:
        print(f"An error occurred: {error}")
        print("Falling back to local CSV storage for survey response.")
        _write_to_csv(SURVEY_CSV, SURVEY_HEADERS, values)
        return error
