class Solution:
    def minNumberOfHours(
        self,
        initialEnergy: int,
        initialExperience: int,
        energy: list[int],
        experience: list[int],
    ) -> int:
        eng = initialEnergy
        exp = initialExperience

        tr_eng = 0
        tr_exp = 0

        for index in range(len(energy)):
            if energy[index] >= eng:
                spread = energy[index] - eng + 1
                tr_eng += spread
                eng += spread

            if experience[index] >= exp:
                spread = experience[index] - exp + 1
                tr_exp += spread
                exp += spread

            exp += experience[index]
            eng -= energy[index]

        return tr_eng + tr_exp


if __name__ == "__main__":
    initialEnergy = 5
    initialExperience = 3
    energy = [1, 4, 3, 2]
    experience = [2, 6, 3, 1]

    energy = [1, 4]
    experience = [2, 5]

    print(
        Solution().minNumberOfHours(
            initialEnergy,
            initialExperience,
            energy,
            experience,
        )
    )
