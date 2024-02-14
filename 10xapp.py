def tenX(file):
    """the average engineer writes 10 lines of code a day"""
    """therefore, by strict definition and in as much good faith as the people who deem 5 years of java a requisite for writing react applications, the requirements to become a 10x engineer are merely to write 100 lines of code a day"""
    """since engineers are busy, we're always looking for ways to streamline redundant processes"""
    """in accordance with these ideals, I have created a script that will help me attain the sought-after 10x engineer title"""
    
    how_many_lines = 100
    pointless_distinction = "print('I am a 10x engineer; the term has deep meaning and sanctity, and as such, ought be treated with the appropriate degree of reverence.')"
    counter = 0
    with open(file, "a") as f:
        while counter < how_many_lines:
            f.write(pointless_distinction + "\n")
            counter += 1

tenX("10xProof.py")