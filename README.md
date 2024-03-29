# goit-algo-hw-04
Python має дві вбудовані функції сортування: sorted і sort. Функції сортування Python використовують Timsort — гібридний алгоритм сортування, що поєднує в собі сортування злиттям і сортування вставками.

Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання. Аналіз повинен бути підтверджений емпіричними даними, отриманими шляхом тестування алгоритмів на різних наборах даних. Емпірично перевірте теоретичні оцінки складності алгоритмів, наприклад, сортуванням на великих масивах. Для заміру часу виконання алгоритмів використовуйте модуль timeit.

Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим, і саме з цієї причини програмісти, в більшості випадків, використовують вбудовані в Python алгоритми, а не кодують самі. Зробіть висновки.
_______________________________________________________________________________________________________

Merge Sort Time: 0.045753000071272254
Insertion Sort Time: 4.661211399943568
Timsort Time: 0.002101300051435828
Найшвидший алгоритм: Timsort

Результати вимірювань можна використати для визначення ефективності кожного алгоритму, який працює з певним набором даних (масив з 1000 елементів в нашому випадку). Тимсорт зазвичай працює швидше за алгоритми сортування злиттям і вставками, оскільки він комбінує ці алгоритми для підвищення продуктивності. Це дозволяє вбудованому сортуванню Python використовувати найефективніший метод для різноманітних типів даних і розмірів масивів.