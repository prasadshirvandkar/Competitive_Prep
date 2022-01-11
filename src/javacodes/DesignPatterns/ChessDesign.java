package javacodes.DesignPatterns;

class Spot {
    int x,y;
    Piece piece;

    void getSpot(){

    }
}

class Piece {
    String name;
    int color;
    boolean isKilled;

    void canMove() {

    }
}

class Player {
    boolean isBlack;
    String name;
}

class Board {
    Board[][] board;

    void init() {
        //Initialize Pieces
    }
}

class Game {

    Player players[];
    //Intializes

    void init() {
        //Board
    }

    void toMove(Spot to, Spot from) {
        this.move();
    }

    void move() {
        
    }

}

public class ChessDesign {
    
}