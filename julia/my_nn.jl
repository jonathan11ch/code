using Flux
using Plots
println("My NN program")

#x = -5:5; plot(x, sigmoid.(x), legend =false)

data_len = 10

function generate_data(data_len::Int)
    x = -data_len:data_len
    y(x) =x^3 - x^2 + x; plot(x,y.(x),legend = false)
    return Flux.Data.DataLoader(x,y.(x), batchsize = 5)
end



function single_neuron()
    return Dense(3,1,sigmoid)
end

data = generate_data(10)
neuron = single_neuron()
opt = Descent(0.05)

loss_function(x,y) = sum(Flux.Losses.mse(neuron(x),y))

params = Flux.params(neuron)

Flux.Optimise.train!(loss_function, params, opt)

#https://fluxml.ai/Flux.jl/stable/models/overview/
