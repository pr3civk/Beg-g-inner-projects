with open(
    ""
) as names_file:
    names = names_file.readlines()
    # print(names)


with open(
    ""
) as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip("\n")
        letter_after_replacement = letter.replace("[name]", stripped_name)
        with open(
            f"../Python/mail_merge/merge_mail/Output/letter_{stripped_name}.txt", "x"
        ) as completed_letter:
            completed_letter.write(letter_after_replacement)
