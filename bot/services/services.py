from handlers.user_handler import database


def analyses(telegram_id):
    client_id = database.get_client_id(telegram_id)
    result_hash = database.get_result(client_id)[0]
    job_alerts = database.get_result_alert(result_hash)
    return job_alerts


def step_result(count: int, options: tuple):
    if count < 0:
        return options[0]
    return options[1]
