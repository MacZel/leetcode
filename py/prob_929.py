class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emails_set = set()
        for email in emails:
            localname, domain = email.split("@")
            plusPos = localname.find("+")
            if plusPos >= 0:
                localname = localname[:plusPos]
            localname = localname.replace(".", "")
            email = "@".join([localname, domain])
            emails_set.add(email)
        return len(emails_set)
