#include <stdio.h>
#include <stdlib.h>

void printArray(int* data, int n) {
    printf("Dữ liệu đã lưu trữ là:\n");
    for (int i = 0; i < n; ++i) {
        printf("%d ", data[i]);
    }
    printf("\n");
}

int isDuplicate(int* data, int n, int element) {
    // Kiểm tra xem phần tử đã tồn tại trong mảng hay chưa
    for (int i = 0; i < n; ++i) {
        if (data[i] == element) {
            return 1;
        }
    }
    return 0;
}

int* addElement(int* data, int* n, int element) {
    // Kiểm tra xem phần tử đã tồn tại trong mảng hay chưa
    if (isDuplicate(data, *n, element)) {
        printf("Lỗi: Phần tử đã tồn tại trong mảng!\n");
        return data;
    }

    // Tăng kích thước mảng lên 1
    int newSize = (*n) + 1;
    int* newData = (int*)realloc(data, newSize * sizeof(int));
    if (newData == NULL) {
        printf("Không đủ bộ nhớ!\n");
        return data; // Trả về mảng gốc nếu không thành công
    }
    data = newData;

    // Thêm phần tử vào cuối mảng
    data[*n] = element;
    (*n)++;

    return data;
}

int* deleteElement(int* data, int* n, int index) {
    // Kiểm tra vị trí hợp lệ
    if (index < 0 || index >= *n) {
        printf("Vị trí không hợp lệ!\n");
        return data;
    }

    // Xóa phần tử tại vị trí index
    for (int i = index; i < (*n) - 1; ++i) {
        data[i] = data[i + 1];
    }

    // Giảm kích thước mảng đi 1
    int newSize = (*n) - 1;
    int* newData = (int*)realloc(data, newSize * sizeof(int));
    if (newData == NULL && newSize > 0) {
        printf("Không đủ bộ nhớ!\n");
        return data; // Trả về mảng gốc nếu không thành công
    }
    data = newData;

    (*n)--;

    return data;
}

void updateElement(int* data, int n, int index, int newValue) {
    // Kiểm tra vị trí hợp lệ
    if (index < 0 || index >= n) {
        printf("Vị trí không hợp lệ!\n");
        return;
    }

    // Kiểm tra xem giá trị mới đã tồn tại trong mảng hay chưa
    if (isDuplicate(data, n, newValue)) {
        printf("Lỗi: Phần tử đã tồn tại trong mảng!\n");
        return;
    }

    // Cập nhật giá trị phần tử tại vị trí index
    data[index] = newValue;
}

int main() {
    int n = 0; 
    int* data = NULL; 

    int choice;
    while (1) {
        printf("Menu:\n");
        printf("1. Thêm phần tử\n");
        printf("2. Xóa phần tử\n");
        printf("3. Cập nhật phần tử\n");
        printf("4. Kết thúc chương trình\n");
        printf("Chọn một tùy chọn: ");
        scanf("%d", &choice);

        if (choice == 1) {
            // Thêm phần tử
            int newElement;
            printf("Nhập phần tử mới: ");
            if (scanf("%d", &newElement) != 1) {
                printf("Lỗi: Phần tử không phải là số nguyên!\n");
                fflush(stdin);
                continue;
            }
            data = addElement(data, &n, newElement);
            printArray(data, n);
        } else if (choice == 2) {
            // Xóa phần tử
            if (n == 0) {
                printf("Không có dữ liệu để xóa!\n");
            } else {
                int deleteIndex;
                printf("Nhập vị trí phần tử cần xóa: ");
                if (scanf("%d", &deleteIndex) != 1) {
                    printf("Lỗi: Vị trí không phải là số nguyên!\n");
                    fflush(stdin);
                    continue;
                }
                data = deleteElement(data, &n, deleteIndex);
                printArray(data, n);
            }
        } else if (choice == 3) {
            // Cập nhật phần tử
            if (n == 0) {
                printf("Không có dữ liệu để cập nhật!\n");
            } else {
                int updateIndex, updateValue;
                printf("Nhập vị trí phần tử cần cập nhật: ");
                if (scanf("%d", &updateIndex) != 1) {
                    printf("Lỗi: Vị trí không phải là số nguyên!\n");
                    fflush(stdin);
                    continue;
                }
                if (updateIndex < 0 || updateIndex >= n) {
                    printf("Vị trí không hợp lệ!\n");
                } else {
                    printf("Nhập giá trị mới: ");
                    if (scanf("%d", &updateValue) != 1) {
                        printf("Lỗi: Giá trị không phải là số nguyên!\n");
                        fflush(stdin);
                        continue;
                    }
                    updateElement(data, n, updateIndex, updateValue);
                    printArray(data, n);
                }
            }
        } else if (choice == 4) {
            // Kết thúc chương trình
            break;
        } else {
            printf("Tùy chọn không hợp lệ!\n");
        }
    }

    free(data);

    return 0;
}