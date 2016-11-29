# template function

# def function_name(things_the_function_needs)
#     results = do_some_stuff_to(things_the_function_needs)
#     return results
# end

# Also makes it easier to find problems. Here we only have to change one character instead of three.

def favorite_book(bookname)
    puts "My favorite book is" + bookname
end

def favorite_movie(movie)
    puts "Anything without raccoons"
    puts "Also I guess " + movie + " is OK"
    something_unexpected
end

favorite_book('Mrs.Dalloway')
favorite_book('Ulysses')
favorite_book('The Amazing Life of Kavalier and Clay')

favorite_movie('Sparticus')

# That error message will get caught and the program will point us to the specific function that is the problem. So you don't have to chase all over the program.