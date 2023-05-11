import random
import csv
import folium
import time


def index():
    list_COLOR = []
    with open('Quantity.txt', 'r') as file:
        number_list = file.read().split(', ')

    with open("temp.txt", "w") as f:
        f.write("Quantity, Color, Address\n")
        for number in number_list:
            if int(number) >= 500:
                color = '#FF1105'
                list_COLOR.append(color)
            elif 200 <= int(number) < 500:
                color = '#F0ED1E'
                list_COLOR.append(color)
            else:
                color = '#1EF013'
                list_COLOR.append(color)
            start_lat = 21.549003662390355
            start_long = 105.84488441687587
            add = [start_lat + random.uniform(-0.004, 0.004), start_long + random.uniform(-0.004, 0.004)]
            add_str = ', '.join(str(x) for x in add)
            line = str(number) + ", " + color + ", [" + add_str + "]\n"
            f.write(line)

    quantity_list = []
    color_list = []
    address_list = []

    with open('temp.txt', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            quantity = row[0].strip()
            quantity_list.append(quantity)
            color = row[1].strip()
            color_list.append(color)
            address = row[2].strip() + ", " + row[3].strip()
            address_list.append(address)

    myMap = folium.Map(location=[21.549003662390355, 105.84488441687587], zoom_start=12)
    # print(address_list)


    # Thêm các địa điểm vào bản đồ
    for address, quantity, color in zip(address_list, quantity_list, color_list):
        lat, long = address.split(', ')
        lat = float(lat.strip('[]'))
        long = float(long.strip(']'))
        address = [lat, long, "Phát hiện có " + quantity + " rác"]
        # Thêm vòng tròn đại diện cho bán kính
        folium.CircleMarker(location=address[:2], radius=20, color=color, popup='Radius: 50 meters').add_to(myMap)
        # Thay đổi popup_html tùy thuộc vào địa chỉ
        popup_html = '<span style="font-size: 20px;">{}</span>'.format(address[2])
        # Thêm đánh dấu và popup cho địa điểm
        folium.Marker(location=address[:2], popup=popup_html, auto_open=True).add_to(myMap)

    # Lưu bản đồ vào tệp HTML
    myMap.save("IP.html")
    print('Đã cập nhật thông tin!')
index()
# if __name__ == '__main__':
#     while True:
#         index()
#         time.sleep(3)
