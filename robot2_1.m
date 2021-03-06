%%------------------------------------------------------------------
%% (c) Juan Gonzalez-Gomez (Obijuan)  juan@iearobotics.com
%% Abril-2012
%%------------------------------------------------------------------
%%- Cinematica de un brazo robot de tres grados de libertad:
%%-- 2 para posicionamiento
%%-- 1 para orientacion
%%------------------------------------------------------------------

%%-- Entradas: Angulos en grados
function robot2_1(q1,q2,q3)

%%-- Pasar los angulos a radianes
q1= q1*pi/180;
q2= q2*pi/180;
q3= q3*pi/180;

%%-- Geometria del robot: 2 eslavones de longitudes l1 y l2
l1 = 1; 
l2 = 1;

%%-- Transformadas homogeneas
A1 = Rotx(q1)*Trasy(l1);  %-- Del sistema 1 al 0
A2 = Rotx(q2)*Trasy(l2);  %-- Del sistema 2 al 1
A3 = Rotx(q3);            %-- Orientacion

%%-- Transformada final
T = A1*A2*A3;

%%-- Calcular las coordenadas de los origenes de los sistemas
P01 = A1*[0 0 0 1]';
P02 = A1*A2*[0 0 0 1]';

%%-- Dibujar robot

y = [0 P01(2) P02(2)];
z = [0 P01(3) P02(3)];

hold off;
plot(y,z,'-o','linewidth',4);
hold on;

%%-- Dibujar la pinza
pinza(T);

l = l1 + l2 + 0.5*l1;
axis([0 l 0 l]);
axis('off');


