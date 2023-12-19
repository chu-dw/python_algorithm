import itertools

def calculate_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def calculate_total_distance(points, center_combination):
    total_distance = 0
    for point in points:
        if point not in center_combination:
            print('cal_p',point,'cal_cen', center_combination)
            distances_to_centers = [calculate_distance(point, center) for center in center_combination]
            total_distance += min(distances_to_centers)
    return total_distance

def brute_force_all_combinations(points, num_centers):
    min_total_distance = float('inf')
    best_centers = []

    # 가능한 센터 조합 생성
    center_combinations = list(itertools.combinations(points, num_centers))
    print('all',center_combinations)

    for center_combination in center_combinations:
        print('f_p',points, 'f_c',center_combination)
        total_distance = calculate_total_distance(points, center_combination)
        print('distance',total_distance)

        # 현재 조합의 거리 합이 최소인 경우 업데이트
        if total_distance < min_total_distance:
            min_total_distance = total_distance
            best_centers = center_combination

    return best_centers

# 센터 개수 입력 받기
num_centers = 2

# 예시 사용법
points = [(0,0), (0,1), (0,2), (0,3), (0,4)]
best_centers = brute_force_all_combinations(points, num_centers)

print(f"{num_centers}개의 센터 중 최적의 센터:", best_centers)






















