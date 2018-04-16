def array_left_rotation(a, k):
    """
    The key point is (I + k) % array_length, 
    which is flexible left rotation.
    """
    # Get list length.
    array_length = len(a)
    # Generate a zero list of length 4.
    new_array = [0 for _ in range(array_length)]
    # The remainder is indexed.
    for i in range(array_length):
        index = (i + k) % array_length
        new_array[i] = a[index]
    # Digital transliteration, Print spaces to separate numbers.
    return ' '.join(map(str, new_array))

print(array_left_rotation([1, 2, 3, 4, 5], 4))
