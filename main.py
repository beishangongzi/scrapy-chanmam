import json
import os


path = "/media/andy/z/python/scrapy_chanmama/ctamap_spider/dataFile/v1/brand/detail/author.json"
with open("res.csv", "a+") as f1:
    for file in os.listdir(path):
    # print(file)
        a = file.split("desc-")[-1]
        name = a.split(".")[0]
    # print(name)
        with open(os.path.join(path, file)) as f:
            datas = json.loads(f.readline())["data"]["list"]
            for data in datas:
                values = list(data.values())
                values.insert(0, name)
                for i in range(len(values)):
                    values[i] = str(values[i])
                # f.write(str(",".join(values))
                # f.write("\n")
                f1.write(",".join(values))
                f1.write("\n")
