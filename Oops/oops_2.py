# Instance variable : Name,Amount,Address,AccountNo
# Instance method : CreateAccount(), DisplayAccountInfo()
# class variable : Bank_name,ROI_On_FD
# class method : DisplayBankInformation

class Bank:
    Bank_name = 'ICICI'
    ROI_On_FD = '12%'

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        self.Name = input('Enter name: ')
        self.Amount = int(input('Enter amount: '))
        self.Address = input('Enter address: ')
        self.AccountNo = int(input('Enter acc.no: '))
    
    def DisplayAccountInfo(self):
        print('Account Details-----------------------')
        print(f'Name: {self.Name}\nAmount: {self.Amount}\nAddress: {self.Address}\nAcc no: {self.AccountNo}\n')

    def DisplayBankInformation(cls):
        print('Bank name:',cls.Bank_name,'\nROI on FD:',cls.ROI_On_FD)

def main():
    User1 = Bank()
    print('Creating 1st account-------------------')
    User1.CreateAccount() 
    User1.DisplayAccountInfo()
    print('BankName:', Bank.Bank_name)
    print('ROIonFD:', Bank.ROI_On_FD)
    User1.DisplayBankInformation()

if __name__ == "__main__":
    main()


    
