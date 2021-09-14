using Flux
using Plots
using BenchmarkTools
#actual model to predict
actual(x) = -8x + 3

#data to train
x_train, x_test = hcat(0:10 ...), hcat(6000:6500 ...)
y_train, y_test = actual.(x_train), actual.(x_test)

#predictive model
predict = Dense(1,1)
#reshape the parameters W and b from the NN to the FLUX format
parameter = Flux.params(predict)
#try predicting with default values
println("Default values prediction:" )
#println(predict(x_train))

#define a loss function
loss(x,y) = Flux.Losses.mse(predict(x), y)
println("Default loss computation")
println(loss(x_train,y_train))

#train the model to improve the prediction
#using the Flux train! function
using  Flux.Optimise: train!
#choose the gradient descent optimizer
opt = Descent(0.01)
#arrange the data to train in a tuple format
data = [(x_train, y_train)]
#data1 = [(hcat(x_train[1:10]...), hcat(y_train[1:10]...))]
#data2 = [(hcat(x_train[1:100]...), hcat(y_train[1:100]...))]
#data3 = [(hcat(x_train[1:1000]...), hcat(y_train[1:1000]...))]

#train the model
train!(loss, parameter, data, opt)
println("After first iteration")
println(loss(x_train, y_train))

function iterative_training!()
    println("iterative_training!")
    for epoch in 1:500
        train!(loss, parameter, data, opt)
        println(loss(x_train, y_train))
    end
    println("final Loss after iterative learning")
    println(loss(x_train, y_train))
end

@time iterative_training!()


#with the model trained perform prediction
plot(x_test',predict(x_test)')
