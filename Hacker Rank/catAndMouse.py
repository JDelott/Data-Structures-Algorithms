# def catAndMouse(x, y, z):
#     if x < y:
#         return x
#     if y > x:
#         return y
#     if x == y:
#         return z


# psuedocode

# check where the first cat is x
# check where the second cat is y
# check where the mouse is z

# if the cat1 is closer to the mouse cat1 wins
# if the cat2 is closer to the mouse cat2 wins
# if both cats are same distance the mouse wins cats lose


def catAndMouse(x, y, z):
    dist_cat_a = abs(z - x)
    dist_cat_b = abs(z - y)

    if dist_cat_a < dist_cat_b:
        return "Cat A"
    if dist_cat_b < dist_cat_a:
        return "Cat B"
    else:
        return "Mouse C"


print(catAndMouse(1, 2, 3))
print(catAndMouse(1, 3, 2))
