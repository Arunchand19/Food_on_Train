trains_db = {
    '12354': {
        'name': 'Charminar Express',
        'start': 'Hyderabad Deccan',
        'destination': 'Tambaram',
        'stations': ['Secunderabad Junction', 'Warangal', 'Vijayawada Junction']
    },
    '17260': {
        'name': 'Telangana Express',
        'start': 'Secunderabad Junction',
        'destination': 'New Delhi',
        'stations': ['Kazipet Junction', 'Nagpur Junction', 'Gwailor Junction']
    },
    '19045': {
        'name': 'kerala Express',
        'start': 'New Delhi',
        'destination': 'Thiruvananthapuram Central',
        'stations': ['Kharagpur Junction', 'Bhubaneswar', 'Chennai Central']
    }
}

restaurants_db = {
    'Secunderabad Junction': [
        (1, 'Restaurant A'),
        (2, 'Restaurant B'),
        (3, 'Restaurant C'),
    ],
    'Warangal': [
        (4, 'Restaurant D'),
        (5, 'Restaurant E'),
        (6, 'Restaurant F'),
    ],
    'Vijayawada Junction': [
        (7, 'Restaurant F'),
        (8, 'Restaurant G'),
    ],
    'Kazipet Junction': [
        (9, 'Restaurant H'),
        (10, 'Restaurant I'),
        (11, 'Restaurant J'),
    ],
    'Nagpur Junction': [
        (12, 'Restaurant J'),
        (13, 'Restaurant K'),
         
    ],
    'Gwailor Junction': [
        (15, 'Restaurant M'),
        (16, 'Restaurant N'),
    ],
    'Kharagpur Junction': [
        (17, 'Restaurant P'),
        (18, 'Restaurant Q'),
    ],
    'Bhubaneswar': [
        (19, 'Restaurant R'),
        (20, 'Restaurant S'),
    ],
    'Chennai central': [
        (21, 'Restaurant T'),
        (22, 'Restaurant U'),
       
    ],
}

menu_db = {
    1: [
        (101, 'chicken Biryani', 199.00, "/static/images/chickenbir.jpg"),
        (102,'chicken Fried Rice', 149.00,"/static/images/mini1.jpg"),
        (103, 'chicken Manchuria', 219.00,"/static/images/mini2.jpg"),
        (104, 'chicken 65', 149.00,"/static/images/mini3.jpg"),
        (105,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (106,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),
        (107, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (108, 'Burger', 119.00, "/static/images/burger.jpg"),
        (109, 'Parota', 49.00, "/static/images/parota.jpg"),
        
    ],
    2: [
        (201, 'chicken special Biryani', 399.00, "/static/images/biryani.jpg"),
        (202, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (203,'apple juice', 149.00,"/static/images/mini8.jpg"),
        (204,'mango juice', 100.00,"/static/images/mini9.jpg"),
        (205, 'Chicken tandoori', 149.00, "/static/images/tandoori.jpg"),
        (206,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (207, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (208, 'Burger', 119.00, "/static/images/burger.jpg"),
        (209, 'Parota', 49.00, "/static/images/parota.jpg"),
    ],
    3: [
        (301, 'Pasta', 249.00,"/static/images/pasta.jpg"),
        (302,'mango juice', 100.00,"/static/images/mini9.jpg"),
        (303, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (304, 'Chicken 555', 249.00,"/static/images/mini3.jpg"),
        (305, 'Burger', 119.00, "/static/images/burger.jpg"),
        (306, 'chicken 65', 149.00,"/static/images/mini3.jpg"),
        (307,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (308,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),

    ],
    4: [
        (101, 'Biryani', 299.00, "/static/images/biryani.jpg"),
        (102, 'Parota', 199.00, "/static/images/parota.jpg"),
        (103, 'Masala Dosa', 199.00, "/static/images/masala.jpg"),
        (104, 'Veg Fried Rice', 299.00, "/static/images/friedrice.jpg"),
        (105, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (106,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (107, 'chicken special Biryani', 399.00, "/static/images/biryani.jpg"),
        (108, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (109,'apple juice', 149.00,"/static/images/mini8.jpg"),
    ],
    5: [
        (201, 'Masala Dosa', 199.00, "/static/images/masala.jpg"),
        (202, 'Veg Fried Rice', 299.00, "/static/images/friedrice.jpg"),
        (203, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (204, 'Chicken 555', 249.00,"/static/images/mini3.jpg"),
        (205, 'Chicken tandoori', 149.00, "/static/images/tandoori.jpg"),
        (206,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (207, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (208, 'Burger', 119.00, "/static/images/burger.jpg"),
        (209, 'Parota', 49.00, "/static/images/parota.jpg"),
        
        
    ],
    6: [
        (301, 'Chicken Tikka Biryani', 399.00, "/static/images/biryani.jpg"),
        (302, 'Chicken Curry', 249.00, "/static/images/curry.jpg"),
        (303, 'Burger', 119.00, "/static/images/burger.jpg"),
        (304, 'Chicken 555', 249.00,"/static/images/mini3.jpg"),
        (305, 'Parota', 49.00, "/static/images/parota.jpg"),
        (306, 'chicken 65', 149.00,"/static/images/mini3.jpg"),
        (307,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (308,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),
    ],
    7: [
        (101, 'Chicken Curry', 249.00, "/static/images/curry.jpg"),
        (102, 'Burger', 119.00, "/static/images/burger.jpg"),
        (103, 'Masala Dosa', 199.00, "/static/images/masala.jpg"),
        (104, 'Veg Fried Rice', 299.00, "/static/images/friedrice.jpg"),
        (105, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (106,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (107, 'chicken special Biryani', 399.00, "/static/images/biryani.jpg"),
        (108, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (109,'apple juice', 149.00,"/static/images/mini8.jpg"),
    ],
    8: [
       (201, 'Veg Fried Rice', 299.00, "/static/images/friedrice.jpg"),
        (202, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (203, 'Chicken 555', 249.00,"/static/images/mini3.jpg"),
        (204,'apple juice', 149.00,"/static/images/mini8.jpg"),
        (205, 'Chicken tandoori', 149.00, "/static/images/tandoori.jpg"),
        (206,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (207, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (208, 'Burger', 119.00, "/static/images/burger.jpg"),
        (209, 'Parota', 49.00, "/static/images/parota.jpg"),
        
    ],
    9: [
        (301,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),
        (302, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (303, 'Chicken 555', 249.00,"/static/images/mini3.jpg"),
        (304, 'Parota', 49.00, "/static/images/parota.jpg"),
        (305, 'Burger', 119.00, "/static/images/burger.jpg"),
        (306, 'chicken 65', 149.00,"/static/images/mini3.jpg"),
        (307,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (308, 'Chicken tandoori', 149.00, "/static/images/tandoori.jpg"),
    ],
    10: [
        (101, 'Chicken tandoori', 249.00, "/static/mini6.jpg"),
        (102, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (103,'apple juice', 149.00,"/static/images/mini8.jpg"),
        (104, 'Veg Fried Rice', 299.00, "/static/images/friedrice.jpg"),
        (105, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (106,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (107, 'chicken special Biryani', 399.00, "/static/images/biryani.jpg"),
        (108,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),
        (109, 'Chicken tandoori', 149.00, "/static/images/tandoori.jpg"),
    ],
    11: [
        (201, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (202,'apple juice', 149.00,"/static/images/mini8.jpg"),
         (203, 'Chicken 555', 249.00,"/static/images/mini3.jpg"),
       (204, 'Veg Fried Rice', 299.00, "/static/images/friedrice.jpg"),
        (205, 'Chicken tandoori', 149.00, "/static/images/tandoori.jpg"),
        (206,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (207, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (208, 'Burger', 119.00, "/static/images/burger.jpg"),
        (209, 'Parota', 49.00, "/static/images/parota.jpg"),
    ],
    12: [
         (301,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),
        (302, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (303, 'Chicken 555', 249.00,"/static/images/mini3.jpg"),
        (304, 'Parota', 49.00, "/static/images/parota.jpg"),
        (305, 'Burger', 119.00, "/static/images/burger.jpg"),
        (306, 'chicken 65', 149.00,"/static/images/mini3.jpg"),
        (307,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (308, 'Chicken tandoori', 149.00, "/static/images/tandoori.jpg"),
    ],
    13: [
         (101, 'chicken Biryani', 199.00, "/static/images/chickenbir.jpg"),
        (102,'chicken Fried Rice', 149.00,"/static/images/mini1.jpg"),
        (103, 'chicken Manchuria', 219.00,"/static/images/mini2.jpg"),
        (104, 'chicken 65', 149.00,"/static/images/mini3.jpg"),
        (105,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (106,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),
        (107, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (108, 'Burger', 119.00, "/static/images/burger.jpg"),
        (109, 'Parota', 49.00, "/static/images/parota.jpg"),
    ],
    14: [
        (201, 'Chicken tandoori', 249.00, "/static/mini6.jpg"),
        (202, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (203,'apple juice', 149.00,"/static/images/mini8.jpg"),
        (204, 'Chicken 555', 249.00,"/static/images/mini3.jpg"),
        (205,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),
        (206,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (207, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (208, 'Burger', 119.00, "/static/images/burger.jpg"),
        (209, 'Parota', 49.00, "/static/images/parota.jpg"),
    ],
    15: [
        (301,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),
        (302, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (303, 'Chicken 555', 249.00,"/static/images/mini3.jpg"),
        (304, 'Parota', 49.00, "/static/images/parota.jpg"),
        (305, 'Burger', 119.00, "/static/images/burger.jpg"),
        (306, 'chicken 65', 149.00,"/static/images/mini3.jpg"),
        (307,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (308, 'Chicken tandoori', 149.00, "/static/images/tandoori.jpg"),
    ],
    16: [
        (101, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (102,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),
         (103, 'chicken Manchuria', 219.00,"/static/images/mini2.jpg"),
        (104, 'chicken 65', 149.00,"/static/images/mini3.jpg"),
        (105,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (106,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),
        (107, 'Chicken tandoori', 149.00, "/static/images/tandoori.jpg"),
        (108, 'Burger', 119.00, "/static/images/burger.jpg"),
        (109, 'Parota', 49.00, "/static/images/parota.jpg"),
    ],
    17: [
         (201,'mango juice', 100.00,"/static/images/mini9.jpg"),
        (202, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (203, 'Chicken 555', 249.00,"/static/images/mini3.jpg"),
        (204, 'Burger', 119.00, "/static/images/burger.jpg"),
        (205, 'Chicken tandoori', 149.00, "/static/images/tandoori.jpg"),
        (206,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (207, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (208,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),
        (209, 'Parota', 49.00, "/static/images/parota.jpg"),
    ],
    18: [
        (301, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (302,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),       
        (303, 'Chicken 555', 249.00,"/static/images/mini3.jpg"),
        (304, 'Parota', 49.00, "/static/images/parota.jpg"),
        (305, 'Burger', 119.00, "/static/images/burger.jpg"),
        (306, 'chicken 65', 149.00,"/static/images/mini3.jpg"),
        (307,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (308, 'Chicken tandoori', 149.00, "/static/images/tandoori.jpg"),
    ],
    19: [
        (101,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),
        (102, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (103,'apple juice', 149.00,"/static/images/mini8.jpg"),
        (104, 'Veg Fried Rice', 299.00, "/static/images/friedrice.jpg"),
        (105, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (106,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (107, 'chicken special Biryani', 399.00, "/static/images/biryani.jpg"),
        (108, 'Chicken tandoori', 149.00, "/static/images/tandoori.jpg"),
        
    ],
    20: [
        (201, 'Chicken tandoori', 249.00, "/static/mini6.jpg"),
        (202, ' Paneer 65', 299.00, "/static/images/mini7.jpg"),
        (203,'apple juice', 149.00,"/static/images/mini8.jpg"),
        (204, 'Burger', 119.00, "/static/images/burger.jpg"),
        (205, 'chicken special Biryani', 399.00, "/static/images/biryani.jpg"),
        (206,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (207, 'Pizza', 299.00, "/static/images/imag1.jpg"),       
        (208, 'Parota', 49.00, "/static/images/parota.jpg"),
    ],
    21: [
        (301, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (302,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),   
        (303, 'Chicken 555', 249.00,"/static/images/mini3.jpg"),
        (304, 'Parota', 49.00, "/static/images/parota.jpg"),
        (305, 'Burger', 119.00, "/static/images/burger.jpg"),
        (306, 'chicken 65', 149.00,"/static/images/mini3.jpg"),
        (307,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (308, 'Chicken tandoori', 149.00, "/static/images/tandoori.jpg"),
    ],
    22: [
       (101, 'chicken Biryani', 199.00, "/static/images/chickenbir.jpg"),
        (102,'chicken Fried Rice', 149.00,"/static/images/mini1.jpg"),
        (103, 'chicken Manchuria', 219.00,"/static/images/mini2.jpg"),
        (104, 'chicken 65', 149.00,"/static/images/mini3.jpg"),
        (105,'veg salads', 149.00,"/static/images/mini4.jpg"),
        (106,'dry fruit salad', 100.00,"/static/images/mini5.jpg"),
        (107, 'Pizza', 299.00, "/static/images/imag1.jpg"),
        (108, 'Burger', 119.00, "/static/images/burger.jpg"),
        (109, 'Parota', 49.00, "/static/images/parota.jpg"),
    ],
    
}


def init_db():
    pass

def get_restaurants_by_station(station_code):
    return restaurants_db.get(station_code, [])

def get_menu_by_restaurant(restaurant_id):
    return menu_db.get(restaurant_id, [])

def get_stations_by_train(train_number):
    return trains_db.get(train_number, [])
