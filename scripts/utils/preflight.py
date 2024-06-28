import logging

from scripts.core.handlers.user_handler import UserHandler


def root_user_check():
    user_handler = UserHandler()
    if not user_handler.get_root_user():
        user_handler.create_root_user()


def run():
    logging.info("Running preflight checks")
    root_user_check()
    logging.info("Preflight checks complete")
