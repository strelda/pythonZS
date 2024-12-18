# Julia is compiled, not interpreted as Python
# that makes it much faster (still slower than C, but not by much)


using Arpack
x = [1. 3.; 4. 5.]
println(x)
eigen(x)



# broadcasting
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
c = a .+ b

sin(x)
sin.(x)



# functions can be defined without types, or with types
function f(x)
    return x^2
end

function g(x::Float64)::Float64
    return x^2
end

g(2)
g(2.0)



function min(λ, 😎)
    😎 < λ  ? 10 : "falsy"
end
min(1, 2)