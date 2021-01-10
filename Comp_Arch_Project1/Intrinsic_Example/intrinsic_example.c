#include <stdio.h>
#include <xmmintrin.h>

int main(){
  float a1[4] = {1.0, 2.0, 3.0, 4.0};
  float a2[4] = {5.0, 6.0, 7.0, 8.0};
  float a3[4] = {0.0, 0.0, 0.0, 0.0};

  __m128 xmm1, xmm2, xmm3;

  xmm1 = _mm_load_ps(a1);
  xmm2 = _mm_load_ps(a2);

  xmm3 = _mm_add_ps(xmm1, xmm2);

  _mm_store_ps(a3, xmm3);

  printf("a3 is %f, %f, %f, %f\n", a3[0], a3[1], a3[2], a3[3]);
  return 0;

}
