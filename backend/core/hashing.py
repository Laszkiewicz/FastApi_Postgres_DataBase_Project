from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)


if __name__ == "__main__":
    hash_pass = Hasher.get_password_hash("Hello")
    print(hash_pass)
    unhash = Hasher.verify_password("Hello", hash_pass)
    print(unhash)
