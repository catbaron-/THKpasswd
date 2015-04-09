class InitPass:
    """Init the passwd.

    This class will try to init a password 
    using the information input from user.
    It's kinds of a Hash algorithm.
    """

    info = {
        "FAMILY_NAME" : "",
        "SCHOOL_CODE" : "",
        "BIRTHDAY" : "",
        "HOME" : ""
    }

    pwd = ""

    def __init__(self):
        """Do nothing here."""
        pass

    def read_info(self, info_type, intro):
        """Read kinds of info"""
        self.info[info_type] = raw_input(intro)
    
    def create_pwd(self):
        """Create pwd"""
        sfn = self.info["FAMILY_NAME"]
        ssc = self.info["SCHOOL_CODE"]
        sbd = self.info["BIRTHDAY"]
        shm = self.info["HOME"]

        isc = int(ssc[0])
        iyear = int(sbd[0:4])
        imonth = int(sbd[4:6])
        iday = int(sbd[6:8])
        
        iyear = (iyear / 1000 + isc) * 1000 + iyear % 1000
        ibd = iyear * imonth * iday

        self.pwd = sfn[0].lower() + ssc[1] + shm + str(ibd)[-5:]

    def start(self):
        self.read_info("FAMILY_NAME", "Family Name: ")
        self.read_info("SCHOOL_CODE", "School Code: ")
        self.read_info("BIRTHDAY", "Birthday: ")
        self.read_info("HOME","Home: ")
        self.create_pwd()
        print "Your Password: " + self.pwd

if __name__ == '__main__':
    print "ok"
    
    ip = InitPass()
    ip.start()
