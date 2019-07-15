/**
 * this program takes a command line input 1 thru 6
 * and displays a typo-graphic image of a dice face
 * with that value.
 *
 *@Author: Dean Bailey
 *
 */
import java.util.*;
import java.io.*;
class DispDiceImage {
    public static void main(String[] args){
	toImage(Integer.parseInt(args[0]));
    }

    //this method outputs the image of the face with value val
    static void toImage(int val) {
        System.out.printf(" _______ \n");
        System.out.printf("|       |\n");
        for (int scanLineNum = 1; scanLineNum <= 3; scanLineNum++) {
            System.out.printf("%s\n", scanLineImage(val, scanLineNum));
        }
        System.out.printf("|_______|\n");
    }
    //this method returns the strings corresponding to scan lines of the face
    static String scanLineImage(int faceVal, int scanLineNum) {
        int patIndex = (faceVal - 1) * 3 + (scanLineNum - 1);
        switch (patIndex) {
        case 0:
        case 2:
        case 4:
        case 10:
            return "|       |";
        case 1:
        case 7:
        case 13:
            return "|   *   |";
        case 3:
        case 6:
            return "|     * |";
        case 5:
        case 8:
            return "| *     |";
        default:
            return "| *   * |";
        }
    }
}
