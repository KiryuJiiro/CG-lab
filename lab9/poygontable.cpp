#include <stdio.h>
#include <conio.h>
#include <graphics.h>

#define WINDOW_WIDTH 800
#define WINDOW_HEIGHT 600
#define MAX_VERTICES 10
#define MAX_EDGES (MAX_VERTICES * (MAX_VERTICES - 1) / 2)

typedef struct {
    int x;
    int y;
} Point;

typedef struct {
    int num_vertices;
    Point vertices[MAX_VERTICES];
} PolygonTable;

typedef struct {
    int vertex1;
    int vertex2;
} Edge;

typedef struct {
    int num_edges;
    Edge edges[MAX_EDGES];
} EdgeTable;

void drawPolygonTable(const PolygonTable* table) {
    for (int i = 0; i < table->num_vertices - 1; i++) {
        line(table->vertices[i].x, table->vertices[i].y, table->vertices[i + 1].x, table->vertices[i + 1].y);
    }
    line(table->vertices[table->num_vertices - 1].x, table->vertices[table->num_vertices - 1].y,
         table->vertices[0].x, table->vertices[0].y);
}

void printVertexTable(const PolygonTable* table) {
    printf("Vertex Table:\n");
    for (int i = 0; i < table->num_vertices; i++) {
        printf("Vertex %d: (%d, %d)\n", i + 1, table->vertices[i].x, table->vertices[i].y);
    }
}

void buildEdgeTable(const PolygonTable* table, EdgeTable* edgeTable) {
    edgeTable->num_edges = 0;
    for (int i = 0; i < table->num_vertices - 1; i++) {
        for (int j = i + 1; j < table->num_vertices; j++) {
            edgeTable->edges[edgeTable->num_edges].vertex1 = i;
            edgeTable->edges[edgeTable->num_edges].vertex2 = j;
            edgeTable->num_edges++;
        }
    }
}

void printEdgeTable(const EdgeTable* edgeTable) {
    printf("\nEdge Table:\n");
    for (int i = 0; i < edgeTable->num_edges; i++) {
        printf("Edge %d: Vertex %d - Vertex %d\n", i + 1, edgeTable->edges[i].vertex1 + 1, edgeTable->edges[i].vertex2 + 1);
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\TC\\BGI");

    PolygonTable polygonTable;
    polygonTable.num_vertices = 4;
    polygonTable.vertices[0] = {100, 100};
    polygonTable.vertices[1] = {200, 100};
    polygonTable.vertices[2] = {200, 200};
    polygonTable.vertices[3] = {100, 200};

    drawPolygonTable(&polygonTable);
    printVertexTable(&polygonTable);

    EdgeTable edgeTable;
    buildEdgeTable(&polygonTable, &edgeTable);
    printEdgeTable(&edgeTable);

    getch();
    closegraph();

    return 0;
}
