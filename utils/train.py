# def check_sanity_of_train_restore(TRAIN_OR_RESTORE):
#     """
#
#     :param TRAIN_OR_RESTORE: pyString
#     :return:
#     """
#     while not (TRAIN_OR_RESTORE.isalpha() and TRAIN_OR_RESTORE.upper() in ['T',
#                                                                            'R']):
#         TRAIN_OR_RESTORE = input(
#             "✘ The format of your input is illegal, please re-input: ")
#     logging.info(
#         "✔︎ The format of your input is legal, now loading to next step...")
