


struct Perceptron{l}
    W::Vector{l}
end


function activation(x)
    if x > 0
        return 1
    else
        return 0
    end
end

#perceptron(x) = activation.(w*x)



#function update_weights(net, data, )
