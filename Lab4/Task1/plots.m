alg1=load('Alg1.txt');
data=load('Data.txt');
alg2=load('Alg2.txt');
alg3=load('Alg3.txt');
alg4=load('Alg4.txt');

figure
title("Сглаживающие алгоритмы")

subplot(2, 2, 1)
plot(data(:,2), data(:,1))
hold on
plot(alg1(:,2), alg1(:,1))
hold off
title("'Завтра как вчера'")

subplot(2, 2, 2)
plot(data(:,2), data(:,1))
hold on
plot(alg2(:,2), alg2(:,1))
hold off
title("Скользящее среднее")

subplot(2, 2, 3)
plot(data(:,2), data(:,1))
hold on
plot(alg3(:,2), alg3(:,1))
hold off
title("Взвешенное среднее")

subplot(2, 2, 4)
plot(data(:,2), data(:,1))
hold on
plot(alg4(:,2), alg4(:,1))
hold off
title("Простое экспоненциальное сглаживание")