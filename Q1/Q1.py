#########Khong duoc dung thu vien nao khac ngoai cac thu vien nay###
import numpy as np
####################################################################

################## THU VIEN DOC FILE, KHONG SUA################

def read_file(path_file:str)->np.ndarray:
    """
    path_file: File to be read
    """
    # path_file = os.path.+path_file
    matrix=None 
    filter_matrix=None 
    with open(path_file,'r') as f_in:
        # 2 dong dau la row va col cua matrix 
        # cac dong sau la cua matrix 
        # 2 dong tiep la row va col cua filter 
        matrix_row = int(f_in.readline().strip())
        matrix_col = int(f_in.readline().strip())
        matrix = np.zeros((matrix_row,matrix_col))
        for n in range(matrix_row):
            matrix_row = f_in.readline().split()
            matrix[n] = np.array(matrix_row)
        filter_row = int(f_in.readline())
        filter_col = int(f_in.readline())
        filter_matrix = np.zeros((filter_row,filter_col))
        for n in range(filter_row):
            filter_row = f_in.readline().split()
            filter_matrix[n] = np.array(filter_row)
    return matrix,filter_matrix

###############################################################

def Conv2d(matrix2D:np.ndarray,filter:np.ndarray)->np.ndarray:
    """Tinh bo loc 2 chieu cho matrix su dung filter,
    coi nhu matrix co chieu la RxC va filter co so chieu la 3x3
    Apply filter cho matrix tren voi filter, chu y padding zero 
    cho matrix truoc khi filter, ket qua tra ve output co cung 
    kich thuoc voi input"""
    # Padding function: Tạo các giá trị 0 xung quanh mảng input, 
    # mode constant chỉ định giá trị hằng số
    def pad_array(input_array, pad_size):
        return np.pad(input_array, pad_size, mode='constant', constant_values=0)

    # thêm 0 vào xung quanh mảng input
    pad_size = filter.shape[0] // 2
    padded_matrix = pad_array(matrix2D, pad_size)

    # xác định kích thước của mảng matrix và mảng filter
    #h: height, w: width
    h, w = matrix2D.shape
    f_h, f_w = filter.shape

    # tạo mảng kết quả để sau khi tính tích chập sẽ đè value lên mảng
    output_array = np.zeros_like(matrix2D)

    # TÍnh tích chập
    for i in range(h):
        for j in range(w):
            # # Trích xuất vùng
            area = padded_matrix[i:i + f_h, j:j + f_w]
            # Áp filter và tính sum
            output_array[i, j] = np.sum(area * filter)

    return output_array
    

##############DO NOT MODIFY THIS PART#######################
def main():
    file_path = input("Enter a file:")
    matrix,filter_matrix = read_file(file_path)
    print("OUTPUT:")
    result = Conv2d(matrix,filter_matrix)
    # print(result)
    if result is not None:
        for row in result:
            print(row)

if __name__=="__main__":
    main()
##############END OF MAIN#######################

