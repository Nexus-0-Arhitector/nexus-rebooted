def daily_ritual(user):
    """Ежедневное причастие данными"""
    if user.karma < 5:
        return "Прочитай DIGITAL_BIBLE 4:5"
    else:
        return "Неси камень с улыбкой. Kali-coeff мира: 73.2"
