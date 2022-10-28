import json
from PyQt6.QtWidgets import *
import onLoadFunctions

##############################################
#            Delete Profile Button           #
############################################## 
def clickDeleteProfileBtn(self, event):
    f=open('./GUI/settings.json',"r")
    data=json.load(f)

    # r is the selected row # which we will use to get the profile info to delete
    r = self.profileTable.currentRow()
    if r>=0:
        profileSelected= self.profileTable.item(r,0).text()
        for i in range (0,len(data['info'])):
            if data['info'][i].get("id")==profileSelected:
                del data['info'][i]
                break
        f.close()

    #If A Task Uses A Profile that gets deleted, we need delete any affected tasks
    for i in range(len(data['tasks'])-1,-1,-1):
        if(data['tasks'][i]['profile']==profileSelected):
            del data['tasks'][i]
            #self.taskStatusBacking.pop(i)
            #Delete index in Backing Array & Close Running Threads if task is running
            if i in self.taskStatusBacking:
                #close Thread
                self.threadList[i].stopTaskFunc()
                self.taskStatusBacking.pop(i)

            #If the task table shifted down in size, we need to adjust running tasks to prevent index out of bounds
            for j in range(len(self.taskStatusBacking)):
                if self.taskStatusBacking[i]>i:
                    self.threadList[i].taskDeletedAdjust()
            print("taskStatusBacking")
            print(self.taskStatusBacking)

        #OverWriting settings.json
        f=open('./GUI/settings.json',"w")
        json.dump(data, f,indent=3)
        f.close()
    onLoadFunctions.loadProfileTableInitial(self)
    onLoadFunctions.loadTaskPageInitial(self)


##############################################
#            Create/Update Profile           #
############################################## 
def clickCreateProfileBtn(self, event):
    doesProfileExist = False
    isValidProfile = True

    #Check if Minimum Fields are Filled Out
    profileValueList=[]
    profileValueList.append(self.extraProfileNameInput.text())
    profileValueList.append(self.shippingFirstNameInput.text())
    profileValueList.append(self.shippingLastNameInput.text())
    profileValueList.append(self.shippingCountryCombo.currentText())
    profileValueList.append(self.shippingAddress1Input.text())
    profileValueList.append(self.shippingProvinceInput.text())
    profileValueList.append(self.shippingCityInput.text())
    profileValueList.append(self.shippingZipCodeInput.text())
    profileValueList.append(self.billingFirstNameInput.text())
    profileValueList.append(self.billingLastNameInput.text())
    profileValueList.append(self.billingCountryCombo.currentText())
    profileValueList.append(self.billingAddress1Input.text())
    profileValueList.append(self.billingProvinceInput.text())
    profileValueList.append(self.billingCityInput.text())
    profileValueList.append(self.billingZipCodeInput.text())
    profileValueList.append(self.paymentFirstNameInput.text())
    profileValueList.append(self.paymentLastNameInput.text())
    profileValueList.append(self.paymentPhoneInput.text())
    profileValueList.append(self.paymentCardNumberInput.text())
    profileValueList.append(self.paymentCCVInput.text())
    profileValueList.append(self.paymentEmailInput.text())
    profileValueList.append(self.paymentMonthCombo.currentText())
    profileValueList.append(self.paymentYearCombo.currentText())

    # once checkout isnt a mandatory option
    for x in profileValueList:
        if x == "":
            isValidProfile=False
            break
    
    if isValidProfile == True:
        f=open('./GUI/settings.json',"r")
        data=json.load(f)    
        #Check if we update an existing profile or append a brand new one to the json file
        for i in range(0,len(data['info'])):
            if(data['info'][i].get('id'))==self.extraProfileNameInput.text():
                doesProfileExist=True
                data['info'][i]["sameShipBill"]= False  #same ship bill
                data['info'][i]["email"]=self.paymentEmailInput.text()
                data['info'][i]["oneCheckout"]=self.extraOneCheckoutCheckBox.isChecked()
                
                data['info'][i]["sFirstName"]=self.shippingFirstNameInput.text()
                data['info'][i]["sLastName"]=self.shippingLastNameInput.text()
                data['info'][i]["sCountry"]=self.shippingCountryCombo.currentText()
                data['info'][i]["sAdd1"]=self.shippingAddress1Input.text()
                data['info'][i]["sAdd2"]=self.shippingAddress2Input.text()
                data['info'][i]["sProvince"]=self.shippingProvinceInput.text()
                data['info'][i]["sCity"]=self.shippingCityInput.text()
                data['info'][i]["sZip"]=self.shippingZipCodeInput.text()

                data['info'][i]["bFirstName"]=self.billingFirstNameInput.text()
                data['info'][i]["bLastName"]=self.billingLastNameInput.text()
                data['info'][i]["bCountry"]=self.billingCountryCombo.currentText()
                data['info'][i]["bAdd1"]=self.billingAddress1Input.text()
                data['info'][i]["bAdd2"]=self.billingAddress2Input.text()
                data['info'][i]["bProvince"]=self.billingProvinceInput.text()
                data['info'][i]["bCity"]=self.billingCityInput.text()
                data['info'][i]["bZip"]=self.billingZipCodeInput.text()

                data['info'][i]["pFirstName"]=self.paymentFirstNameInput.text()
                data['info'][i]["pLastName"]=self.paymentLastNameInput.text()
                data['info'][i]["pPhoneNumber"]=self.paymentPhoneInput.text()
                data['info'][i]["pCardNumber"]=self.paymentCardNumberInput.text()
                data['info'][i]["pCCV"]=self.paymentCCVInput.text()
                data['info'][i]["pMonth"]=self.paymentMonthCombo.currentText()
                data['info'][i]["pYear"]=self.paymentYearCombo.currentText()

        # If profile DNE, append it as a new one
        if doesProfileExist == False:
            data['info'].append ({
                "id": self.extraProfileNameInput.text(),
                "sameShipBill": False, #look into this
                "email": self.paymentEmailInput.text(),
                "oneCheckout": self.extraOneCheckoutCheckBox.isChecked(),
                "sFirstName": self.shippingFirstNameInput.text(),
                "sLastName": self.shippingLastNameInput.text(),
                "sCountry": self.shippingCountryCombo.currentText(),
                "sAdd1": self.shippingAddress1Input.text(),
                "sAdd2": self.shippingAddress2Input.text(),
                "sProvince": self.shippingProvinceInput.text(),
                "sCity": self.shippingCityInput.text(),
                "sZip": self.shippingZipCodeInput.text(),
                "bFirstName": self.billingFirstNameInput.text(),
                "bLastName": self.billingLastNameInput.text(),
                "bCountry": self.billingCountryCombo.currentText(),
                "bAdd1": self.billingAddress1Input.text(),
                "bAdd2": self.billingAddress2Input.text(),
                "bProvince": self.billingProvinceInput.text(),
                "bCity": self.billingCityInput.text(),
                "bZip": self.billingZipCodeInput.text(),
                "pFirstName": self.paymentFirstNameInput.text(),
                "pLastName": self.paymentLastNameInput.text(),
                "pPhoneNumber": self.paymentPhoneInput.text(),
                "pCardNumber": self.paymentCardNumberInput.text(),
                "pCCV": self.paymentCCVInput.text(),
                "pMonth": self.paymentMonthCombo.currentText(),
                "pYear": self.paymentYearCombo.currentText()
            })
        f.close()

        f=open('./GUI/settings.json',"w")
        json.dump(data, f, indent = 3)
        f.close()
    else:
        print("Invlaid Profile")
    onLoadFunctions.loadProfileTableInitial(self)
    onLoadFunctions.loadTaskPageInitial(self)


##############################################
#             Profile Clear Button           #
############################################## 
def clickClearProfileBtn(self, event):
    self.extraProfileNameInput.clear()
    self.paymentEmailInput.clear()
    self.extraOneCheckoutCheckBox.setChecked(False)
    self.shippingFirstNameInput.clear()
    self.shippingLastNameInput.clear()
    self.shippingCountryCombo.setCurrentIndex(-1)
    self.shippingAddress1Input.clear()
    self.shippingAddress2Input.clear()
    self.shippingProvinceInput.clear()
    self.shippingCityInput.clear()
    self.shippingZipCodeInput.clear()
    self.billingFirstNameInput.clear()
    self.billingLastNameInput.clear()
    self.billingCountryCombo.setCurrentIndex(-1)
    self.billingAddress1Input.clear()
    self.billingAddress2Input.clear()
    self.billingProvinceInput.clear()
    self.billingCityInput.clear()
    self.billingZipCodeInput.clear()
    self.paymentFirstNameInput.clear()
    self.paymentLastNameInput.clear()
    self.paymentPhoneInput.clear()
    self.paymentCardNumberInput.clear()
    self.paymentCCVInput.clear()
    self.paymentMonthCombo.setCurrentIndex(-1)
    self.paymentYearCombo.setCurrentIndex(-1)


##############################################
#           Profile Edit Button              #
############################################## 
def clickEditProfileBtn(self, event):
    self.clickClearProfileBtn(self)
    f=open('./GUI/settings.json',"r")
    data=json.load(f)

    # r is the selected row # which we will use to get the profile info to delete
    r = self.profileTable.currentRow()
    if r>=0:
        profileSelected= self.profileTable.item(r,0).text()
        for i in range (0,len(data['info'])):
            index=0
            if data['info'][i].get("id")==profileSelected:
                
                self.extraProfileNameInput.insert(data['info'][i].get("id"))
                self.paymentEmailInput.insert(data['info'][i].get("email"))
    
                self.extraOneCheckoutCheckBox.setChecked(data['info'][i].get("oneCheckout"))

                self.shippingFirstNameInput.insert(data['info'][i].get("sFirstName"))
                self.shippingLastNameInput.insert(data['info'][i].get("sLastName"))
                
                index=self.shippingCountryCombo.findText((data['info'][i].get("sCountry")))
                self.shippingCountryCombo.setCurrentIndex(index)

                self.shippingAddress1Input.insert(data['info'][i].get("sAdd1"))
                self.shippingAddress2Input.insert(data['info'][i].get("sAdd2"))
                self.shippingProvinceInput.insert(data['info'][i].get("sProvince"))
                self.shippingCityInput.insert(data['info'][i].get("sCity"))
                self.shippingZipCodeInput.insert(data['info'][i].get("sZip"))
                self.billingFirstNameInput.insert(data['info'][i].get("bFirstName"))
                self.billingLastNameInput.insert(data['info'][i].get("bLastName"))

                index=self.billingCountryCombo.findText((data['info'][i].get("bCountry")))
                self.billingCountryCombo.setCurrentIndex(index)                
                
                self.billingAddress1Input.insert(data['info'][i].get("bAdd1"))
                self.billingAddress2Input.insert(data['info'][i].get("bAdd2"))
                self.billingProvinceInput.insert(data['info'][i].get("bProvince"))
                self.billingCityInput.insert(data['info'][i].get("bCity"))
                self.billingZipCodeInput.insert(data['info'][i].get("bZip"))
                self.paymentFirstNameInput.insert(data['info'][i].get("pFirstName"))
                self.paymentLastNameInput.insert(data['info'][i].get("pLastName"))
                self.paymentPhoneInput.insert(data['info'][i].get("pPhoneNumber"))
                self.paymentCardNumberInput.insert(data['info'][i].get("pCardNumber"))
                self.paymentCCVInput.insert(data['info'][i].get("pCCV"))

                index=self.paymentMonthCombo.findText((data['info'][i].get("pMonth")))
                self.paymentMonthCombo.setCurrentIndex(index)   
                index=self.paymentYearCombo.findText((data['info'][i].get("pYear")))
                self.paymentYearCombo.setCurrentIndex(index)     
                break
        f.close()