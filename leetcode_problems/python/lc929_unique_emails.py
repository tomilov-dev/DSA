class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        map: dict[str, set[str]] = dict()
        for email in emails:
            name = []
            domain = []
            dstart = False
            search_a = False
            for char in email:
                if search_a and char != "@":
                    continue
                elif search_a and char == "@":
                    search_a = False

                if char == "@":
                    dstart = True

                if dstart:
                    domain.append(char)

                else:
                    if char == "+":
                        search_a = True
                    elif char == ".":
                        continue
                    else:
                        name.append(char)

            name = "".join(name)
            domain = "".join(domain)
            if domain not in map:
                map[domain] = set()
            map[domain].add(name)

        count = 0
        for dom, dom_emails in map.items():
            count += len(dom_emails)

        return count


if __name__ == "__main__":
    emails = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com",
    ]
    print(Solution().numUniqueEmails(emails))
