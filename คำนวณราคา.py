"""1.ร้านขายหนังสือร้านหนึ่ง พยายามเพิ่มยอดขายโดยการเสนอโปรโมชั่นพิเศษ ถ้าคุณซื้อหนังสือมากกว่า 3 เล่ม
ที่มีมูลค่ารวมเกิน 500 บาท คุุณจะได้ส่วนลด 10%"""
'''ให้เขียนโปรแกรมรับจำนวนหนังสือที่ซื้อและราคารวม จากนั้นคำนวณราคาที่ต้องจ่าย'''
book = int(input())
price = int(input())
print('How many book: {}'.format(book))
print('How much: {}'.format(price))
if book > 3 and price > 500:
    print('You have to pay {} bath' .format(price * (100 - 10) / 100))
else:
    print('You have to pay {}' .format(price))
