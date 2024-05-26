from utils import syntactic_check
import re


def syntactic_repair(code) -> object:
    if syntactic_check.is_syntactic_correct(code):
        return False, code
    else:
        stop_point = [";", "}", "{", " "]  # 停止符
        for i in range(len(code) - 1, -1, -1):
            # print(code[i])
            if code[i] in stop_point:
                code = code[:i + 1]
                break
        # 检查大括号完整性
        left_bracket = code.count("{")
        right_bracket = code.count("}")
        for idx in range(left_bracket - right_bracket):
            code += "}\n"
        if syntactic_check.is_syntactic_correct(code):
            return True, code
        else:
            matches = list(re.finditer(r"(?<=\})[^\}]+(?=@)", code))
            if matches:
                code = code[:matches[-1].start() + 1]
                left_count = code.count("{")
                right_count = code.count("}")
                for _ in range(left_count - right_count):
                    code += "\n}"
            if syntactic_check.is_syntactic_correct(code):
                return True, code
            else:
                return True, code


def repair_package(code, package_info):
    """
    Repair package declaration in test.
    """
    first_line = code.split('import')[0]
    if package_info == '' or package_info in first_line:
        return code
    code = package_info + "\n" + code
    return code



if __name__ == '__main__':
    code_raw = """Here is a whole JUnit test for the methods of the AVLTree class:

```
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
import java.util.Random;

public class AVLTreeTest {
  
  private AVLTree<Integer> avlTree;

  @Before
  public void setUp() {
    avlTree = new AVLTree<>();
  }

  @Test
  public void testInsert() {
    avlTree.insert(5);
    avlTree.insert(3);
    avlTree.insert(7);
    avlTree.insert(2);
    avlTree.insert(4);
    avlTree.insert(6);
    avlTree.insert(8);

    assertFalse(avlTree.isEmpty());
    assertEquals("2 3 4 5 6 7 8 ", avlTree.serializeInfix());
  }

  @Test
  public void testRemove() {
    avlTree.insert(5);
    avlTree.insert(3);
    avlTree.insert(7);
    avlTree.insert(2);
    avlTree.insert(4);
    avlTree.insert(6);
    avlTree.insert(8);

    avlTree.remove(3);
    avlTree.remove(6);

    assertEquals("2 4 5 7 8 ", avlTree.serializeInfix());
  }

  @Test
  public void testFindMin() {
    avlTree.insert(5);
    avlTree.insert(3);
    avlTree.insert(7);
    avlTree.insert(2);
    avlTree.insert(4);
    avlTree.insert(6);
    avlTree.insert(8);

    int min = avlTree.findMin();
    assertEquals(2, min);
  }

  @Test
  public void testFindMax() {
    avlTree"""
    # print(code)
    if syntactic_check.is_syntactic_correct(code_raw) is False:
        code_after_repair = syntactic_repair(code_raw)
    print(code_after_repair)
