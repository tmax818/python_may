
-- Query: Create 5 different authors: Jane Austen, Emily Dickinson, Fyodor Dostoevsky, William Shakespeare, Lau Tzu

-- Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby

-- Query: Change the name of the C Sharp book to C#

-- Query: Change the first name of the 4th author to Bill

-- Query: Have the first author favorite the first 2 books

-- Query: Have the second author favorite the first 3 books

-- Query: Have the third author favorite the first 4 books

-- Query: Have the fourth author favorite all the books

-- Query: Retrieve all the authors who favorited the 3rd book

SELECT * FROM authors 
JOIN favorites ON authors.id = favorites.author_id
JOIN books ON books.id = favorites.book_id WHERE book_id = 3;

-- Query: Remove the first author of the 3rd book's favorites

-- Query: Add the 5th author as an other who favorited the 2nd book

-- Find all the books that the 3rd author favorited

SELECT books.* FROM books 
JOIN favorites ON books.id = favorites.book_id
WHERE author_id = 3; 

-- Query: Find all the authors that favorited to the 5th book

SELECT books.*, authors.name FROM books
LEFT JOIN favorites ON books.id = favorites.book_id
LEFT JOIN authors ON authors.id = favorites.author_id;

SELECT * FROM authors
LEFT JOIN favorites ON favorites.author_id = authors.id
LEFT JOIN books ON favorites.book_id = books.id;