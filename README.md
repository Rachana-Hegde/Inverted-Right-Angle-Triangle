# 🔻 Inverted Right-Angle Triangle – Python Program

This is a simple Python program that prints an **inverted right-angle triangle pattern** using asterisks (`*`). The pattern begins with a full row of stars and reduces by one star per row.

## 📌 Description

* The user inputs an integer `a`, which defines the height (or number of rows) of the triangle.
* The first row contains `a` stars.
* Each subsequent row starts and ends with a `*`, with the number of middle stars decreasing with each line.

### 🧾 Sample Input & Output

**Input:**

```
Enter height: 5
```

**Output:**

```
* * * * * 
* * * * 
* * * 
* * 
* 
```

> The triangle is **inverted** and aligned to the left, with the top row full of stars and the bottom row containing a single star.

## 🧠 Logic

* First `for` loop prints the full top row with `a` stars.
* Second set of nested loops:

  * Outer loop controls the number of remaining rows (`a - 1`).
  * Inner print statement prints decreasing numbers of stars each time.
  * Ensures one `*` at the start of each row for edge alignment.

## 🛠️ How to Run

1. Save the code in a file like `inverted_triangle.py`.
2. Run the file using Python:
```bash
python inverted_triangle.py
```
3. Enter a positive integer when prompted to see the inverted triangle pattern.

## 🎯 Use Case

* Ideal for beginners practicing:
  * Nested loops
  * Pattern printing
  * Loop-based conditionals

* Can be enhanced to:
  * Center-align the triangle
  * Use different symbols
  * Print hollow versions

## 📬 Contact  

For any inquiries or feedback, feel free to reach out:    
🔗 **GitHub**: [Rachana-Hegde](https://github.com/Rachana-Hegde) 
