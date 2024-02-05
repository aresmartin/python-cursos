def get_product(**datos):  # **kwargs
    print(datos["id"], datos["name"])


get_product(id="23",
            name="iphone",
            desc="Esto es un iphone")
