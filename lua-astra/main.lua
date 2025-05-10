Astra.port = 8080

Astra:get("/", function()
    return "hello!"
end)


Astra:run()
