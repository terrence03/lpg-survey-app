# %%
import os
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# 設定 API 權限範圍
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
]


def get_service_account_credentials() -> service_account.Credentials:
    """從設定檔案獲取服務帳戶認證資訊並建立憑證"""
    # 從TOML配置構建服務帳戶資訊
    service_account_info = st.secrets["gcp_service_account"]

    # 建立憑證物件
    credentials = service_account.Credentials.from_service_account_info(
        service_account_info, scopes=SCOPES
    )

    return credentials


def append_values(values):
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
                spreadsheetId=st.secrets["spreadsheet"]["spreadsheet_id"],
                range="A1:P1",
                valueInputOption="USER_ENTERED",
                body=body,
            )
            .execute()
        )
        print(f"{(result.get('updates').get('updatedCells'))} cells appended.")
        return result

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
