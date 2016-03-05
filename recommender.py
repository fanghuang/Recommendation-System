u0 = ['a1']
u1 = ['a1', 'a2', 'a3', 'a4']
u2 = ['a1', 'a2', 'a3', 'a4']
u3 = ['a5', 'a6', 'a7', 'a8']
u4 = ['a1', 'a2', 'a5']
u5 = ['a1', 'a2', 'a5', 'a6', 'a7', 'a8']

import math

class Helper(object):
	
	@classmethod
	def cosine_similarity(self, place_lst1, place_lst2):
		match_count = self.__count_match(place_lst1,place_lst2)
		return float(match_count) / math.sqrt(len(place_lst1) * len(place_lst2))

	@classmethod
	def __count_match(self, lst1, lst2):
		count = 0
		for i in lst1:
			if i in lst2:
				count += 1
		return count

def recommend_top_5(place, user_history):
	place_similarity = {}
	for places in user_history:
		similarity = Helper.cosine_similarity([place], places)
		for i in places:
			if place_similarity.has_key(i):
				place_similarity[i] += similarity
			else:
				place_similarity[i] = similarity

	if not place_similarity.has_key(place):
		return "This is a brand new place that no one has ever visited here before"

	place_similarity.pop(place)
	sorted_place = sorted(place_similarity.items(), key=lambda x:x[1], reverse=True)
	return sorted_place

print recommend_top_5('a1', [u1,u4])
