## Reverse prints each character in a string on separate lines
print("1)")
text = 'Lab Assignments Strings'
charCount = len(text) - 1

while -1 < charCount:
    print(text[charCount - 1:charCount])
    charCount -= 1

## Returns the number of times the letter appears in a string
print("2)")
def count(parseText, letter):
    i = 0
    total = 0
    while i < len(parseText):
        if letter == parseText[i]:
            total += 1
        i += 1
    return total

sampleText = "apples and bananas"
sampleChar = "a"
print("The string ", sampleText, "has",count(sampleText,sampleChar), "instances of", sampleChar)
print("\n")

## Extracts portion of string after the colon; converts extraction to a floating
print("3)")
strSample = 'X-DSPAM-Confidence: 0.8475'
startPoint = strSample.find(":") + 2
endPoint = len(strSample)
toFloat = float(strSample[startPoint:endPoint])

print(toFloat, type(toFloat))
