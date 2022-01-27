import random
import sys

from mimesis import (
    Person,
    Text,
    Address,
    Datetime,
)
from database import get_session
from tables import (
    User,
    Phone,
    Email,
)


def generate_users(count):
    person = Person("ru")
    text = Text()
    date = Datetime()
    address = Address("ru")

    session = next(get_session())

    for _ in range(count):
        user = User(
            FIO=person.full_name(),
            avatar=text.text(8),
            sex="Male",
            birthdate=date.date(start=1900, end=2018),
            address=address.address()
        )
        session.add(user)

        session.flush()

        user_phone = Phone(
            user_id=user.id,
            kind=random.choice(("mobile", "landline")),
            phone_number=person.telephone()
        )
        session.add(user_phone)

        user_email = Email(
            user_id=user.id,
            kind=random.choice(("work", "home")),
            email=person.email(),
        )
        session.add(user_email)

    try:
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()


def main():
    if len(sys.argv) != 2:
        print("Введите количество пользователей, которое нужно сгенерировать")
        sys.exit()

    count = sys.argv[1]
    if not count.isdigit():
        print("Введите корректное количество пользователей")
        sys.exit()
    count = int(count)
    generate_users(count)


if __name__ == "__main__":
    main()
