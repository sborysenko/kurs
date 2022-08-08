import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("dataframe.csv")


def plot(x, y, x_title, y_title, title):
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y)
    plt.xlabel(x_title, fontsize=15)
    plt.ylabel(y_title, fontsize=15)
    plt.title(title, fontsize=18)


# # Місяць з початку спостережень і ціни на житло
# plot(data.loc[data['rooms'] == 1]["month"], data.loc[data['rooms'] == 1]["price_usd"], "Місяць", "Середня вартість", "Вартість однокімнатних квартир по місяцях")
# plot(data.loc[data['rooms'] == 2]["month"], data.loc[data['rooms'] == 2]["price_usd"], "Місяць", "Середня вартість", "Вартість двокімнатних квартир по місяцях")
# plot(data.loc[data['rooms'] == 3]["month"], data.loc[data['rooms'] == 3]["price_usd"], "Місяць", "Середня вартість", "Вартість трикімнатних квартир по місяцях")
# plot(data.loc[data['rooms'] == 4]["month"], data.loc[data['rooms'] == 4]["price_usd"], "Місяць", "Середня вартість", "Вартість чотрьохкімнатних квартир по місяцях")
# plt.show()
#
# # Район і ціни на житло
# plot(data.loc[data['rooms'] == 1]["district"], data.loc[data['rooms'] == 1]["price_usd"], "Район", "Середня вартість", "Вартість однокімнатних квартир по районах")
# plot(data.loc[data['rooms'] == 2]["district"], data.loc[data['rooms'] == 2]["price_usd"], "Район", "Середня вартість", "Вартість двокімнатних квартир по районах")
# plot(data.loc[data['rooms'] == 3]["district"], data.loc[data['rooms'] == 3]["price_usd"], "Район", "Середня вартість", "Вартість трикімнатних квартир по районах")
# plot(data.loc[data['rooms'] == 4]["district"], data.loc[data['rooms'] == 4]["price_usd"], "Район", "Середня вартість", "Вартість чотрьохкімнатних квартир по районах")
# plt.show()

# Кількість кімнат і ціни на житло
plot(data["rooms"], data["price_usd"], "Загаьна площа", "Середня вартість", "Вартість однокімнатних квартир від загальної площі")
plt.show()

# # Загальна площа і ціни на житло
# plot(data.loc[data['rooms'] == 1]["area"], data.loc[data['rooms'] == 1]["price_usd"], "Загаьна площа", "Середня вартість", "Вартість однокімнатних квартир від загальної площі")
# plot(data.loc[data['rooms'] == 2]["area"], data.loc[data['rooms'] == 2]["price_usd"], "Загаьна площа", "Середня вартість", "Вартість двокімнатних квартир від загальної площі")
# plot(data.loc[data['rooms'] == 3]["area"], data.loc[data['rooms'] == 3]["price_usd"], "Загаьна площа", "Середня вартість", "Вартість трикімнатних квартир від загальної площі")
# plot(data.loc[data['rooms'] == 4]["area"], data.loc[data['rooms'] == 4]["price_usd"], "Загаьна площа", "Середня вартість", "Вартість чотрьохкімнатних квартир від загальної площі")
# plt.show()

corr = data.corr()
print(corr)
# plt.matshow(corr)
sns.heatmap(corr, annot=True)
plt.title("Матриця кореляціі", fontsize=18)
plt.show()
