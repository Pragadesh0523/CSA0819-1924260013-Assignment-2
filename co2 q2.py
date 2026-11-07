def verify(attempts=0):
    if attempts == 3:
        print("Account locked for 30 minutes.")
        return
    otp = input("Enter OTP: ")
    if otp == "":
        return verify(attempts)
    if otp == "1234":
        print("OTP verified successfully!")
        return
    print("Wrong OTP!")
    verify(attempts + 1)
verify()
