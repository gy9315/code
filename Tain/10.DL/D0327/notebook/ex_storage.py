import torch
def print_storage(obj:torch.tensor,name):
    print(f'\n=====[{name}] 기본정보 =====')
    print(f'Shape: {obj.shape}')
    print(f'Ndim: {obj.ndim}') 
    print(f'Dtype: {obj.dtype}')
    print(f'itemsize: {obj.itemsize}')
    print(f'=====STORAGE=====')
    print(f'Offset: {obj.storage_offset()}')
    print(f'Strides: {obj.stride()}')
    print('===================')
    print(obj.untyped_storage())
    
a=torch.tensor([[1,2,3,4,5],[3,6,9,12,15]],dtype=torch.int8)


# 텐서 형태변경
a1=a.transpose(0,1)
print(a1.is_contiguous())
a1=a1.contiguous()

a1=a1.reshape(1,10)
# print(a1)
print_storage(a1,'a1')
# a2=torch.tensor([[1,3],[2,6,],[3,9],[4,12],[5,15]],dtype=torch.uint8)
# print(a2.view(10