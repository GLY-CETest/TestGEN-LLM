code = """import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
public class AVLTreeTest {
  private AVLTree<Integer> tree;
  @Test
  public void testMakeEmpty() {
    tree.insert(5);
    assertFalse(tree.isEmpty());
    tree.makeEmpty();
    assertTrue(tree.isEmpty())"""
stop_point = [";", "}", "{", " "]  # Stop point
for i in range(len(code) - 1, -1, -1):
    print(code[i])
    if code[i] in stop_point:
        print(code[i])
        code = code[:i + 1]
        break
left_bracket = code.count("{")
right_bracket = code.count("}")
for idx in range(left_bracket - right_bracket):
    code += "}\n"

print(code)
print(right_bracket)
print(left_bracket)
