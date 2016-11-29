# template function

# def function_name(things_the_function_needs)
#     results = do_some_stuff_to(things_the_function_needs)
#     return results
# end

# Also makes it easier to find problems. Here we only have to change one character instead of three.

def favorite_book(bookname)
    puts "My favorite book is" + bookname
end

favorite_book('Mrs.Dalloway')
favorite_book('Ulysses')
favorite_book('The Amazing Life of Kavalier and Clay')

# Now it's a lot easier to do the same thing later. Don't have to rewrite the logic.