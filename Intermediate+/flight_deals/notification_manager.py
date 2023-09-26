import smtplib

MY_EMAIL = "...@gmail.com"
MY_PASSWORD = "password"


class NotificationManager:
    @staticmethod
    def send_notification(send_to, flight):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in send_to:
                connection.sendmail(MY_EMAIL, email, msg=f"Subject:BEST FLIGHT DEALS!!!\n\n{flight}")
