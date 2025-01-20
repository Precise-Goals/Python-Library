def httpStatus(t):
    match t:
        case 200: return "Ok"
        case 404: return "Not Found"
        case 500: return "Internal Server Error"
        case _: return "Unknown Status"


print(httpStatus(400))
print(httpStatus(500))
print(httpStatus(404))
print(httpStatus(200))
print(httpStatus(254))
