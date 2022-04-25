# def names(*args):
#     print(args)
    
# names("Kurmanbek", "Muntasir", "Diana", "Faha", "IT RUN")

# def elon_mask(name, *company):
#     print(name)
#     for i in company:
#         print(i)

# elon_mask("Elon", "Tesla", "Space X", "paipal", "StarLink")


def traslate(**words):
    for k, v in words.items():
        print(k, v)
traslate(USA = "США", Kyrgyzstan = "Кыргызстан")