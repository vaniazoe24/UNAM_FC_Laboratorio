% Ubicaciones ideales (Creencia inicial del sistema)
ideal(estante_bebidas, [cerveza, refresco]).
ideal(estante_comida, [sopa, cereal]).
ideal(estante_pan, [galletas]).

% Estado actual (Hechos dinámicos que Python actualizará tras la observación)
% Ejemplo de un estado con desorden (Caso 1.2 b)
ubicado_en(estante_bebidas, refresco).
ubicado_en(estante_bebidas, cerveza).
ubicado_en(estante_bebidas, sopa). % Producto desacomodado
ubicado_en(estante_comida, cereal).
ubicado_en(estante_pan, galletas).

% Regla de Diagnóstico: Identifica qué productos no están en su lugar [cite: 19]
diagnostico(Producto, EstanteActual, EstanteCorrecto) :-
    ubicado_en(EstanteActual, Producto),
    ideal(EstanteCorrecto, ProductosIdeales),
    member(Producto, ProductosIdeales),
    EstanteActual \= EstanteCorrecto.

% Regla de Planificación: Genera las acciones necesarias [cite: 24]
plan(entregar(P)) :- ubicado_en(_, P).
plan(acomodar(P, Destino)) :- diagnostico(P, _, Destino).